from __future__ import (unicode_literals, division, absolute_import, print_function)

import os
from pygit2 import Repository, discover_repository, GIT_STATUS_WT_MODIFIED, GIT_STATUS_WT_DELETED, GIT_STATUS_WT_RENAMED, GIT_STATUS_WT_NEW
from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info, requires_filesystem_watcher

def get_directory(segment_info):
	return segment_info['getcwd']()

def get_repo(dir):
	repo_dir = discover_repository(dir)
	if repo_dir is None:
		return None
	try:
		repo = Repository(repo_dir)
	except Exception:
		return None
	else:
		return repo

@requires_filesystem_watcher
@requires_segment_info
class BasePathSegment(Segment):
	divider_highlight_group = None

	@staticmethod
	def get_best_path(name):
		repo = get_repo(name)
		if repo is None:
			return name
		else:
			return os.path.dirname(os.path.dirname(repo.workdir))

	def __call__(self, pl, segment_info, create_watcher, status_colors=False, ignore_statuses=()):
		name = get_directory(segment_info)
		if name:
			return [{
				'contents': self.get_best_path(name),
				'highlight_groups': ['git_base_path']
			}]


git_base_path = with_docstring(BasePathSegment(),
'''Return the current directory or the base path of a git project.

Highlight groups used: ``git_base_path``.
''')


@requires_filesystem_watcher
@requires_segment_info
class ProjectSegment(Segment):
	divider_highlight_group = None

	@staticmethod
	def get_project(repo):
		return os.path.basename(os.path.dirname(repo.workdir))

	def __call__(self, pl, segment_info, create_watcher, status_colors=False, ignore_statuses=()):
		name = get_directory(segment_info)
		if name:
			repo = get_repo(name)
			if repo is not None:
				return [{
					'contents': self.get_project(repo),
					'highlight_groups': ['git_project']
				}]


git_project = with_docstring(ProjectSegment(),
'''Return the current git project.

Highlight groups used: ``git_project``.
''')


@requires_filesystem_watcher
@requires_segment_info
class ProjectPathSegment(Segment):
	divider_highlight_group = None

	@staticmethod
	def get_project_path(name, repo):
		path = name[len(os.path.dirname(repo.workdir)):]
		if path == "":
			return "/"
		else:
			return path

	def __call__(self, pl, segment_info, create_watcher, status_colors=False, ignore_statuses=()):
		name = get_directory(segment_info)
		if name:
			repo = get_repo(name)
			if repo is not None:
				return [{
					'contents': self.get_project_path(name, repo),
					'highlight_groups': ['git_project_path']
				}]


git_project_path = with_docstring(ProjectPathSegment(),
'''Return the path within the git project.

Highlight groups used: ``git_project_path``.
''')


@requires_filesystem_watcher
@requires_segment_info
class StatusSegment(Segment):
	divider_highlight_group = None

	@staticmethod
	def get_status(repo):
		status = set()
		for filepath, flags in repo.status().items():
			if flags == GIT_STATUS_WT_MODIFIED or flags == GIT_STATUS_WT_DELETED or flags == GIT_STATUS_WT_RENAMED:
				status.add("*")
			if flags == GIT_STATUS_WT_NEW:
				status.add("+")
		if len(status) == 0:
			return None
		return ''.join(status)

	def __call__(self, pl, segment_info, create_watcher, status_colors=False, ignore_statuses=()):
		name = get_directory(segment_info)
		if name:
			repo = get_repo(name)
			if repo is not None:
				status = self.get_status(repo)
				if status is not None:
					return [{
						'contents': status,
						'highlight_groups': ['git_status']
					}]


git_status = with_docstring(StatusSegment(),
'''Return git project status.

Highlight groups used: ``git_status``.
''')
