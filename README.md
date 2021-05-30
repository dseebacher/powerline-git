# Powerline git

Provides some additional segments related to git repositories.

# Install

After cloning the repo install the functions locally with
```
pip3 install ./
```

# Usage

You can then use the segments in your powerline configuration, e.g.
```
{
  "function": "powerline-git.segments.git_project",
  "priority": 10
}
```

## Available segments

* `powerline-git.segments.git_base_path`: the parent path of the local git repo
* `powerline-git.segments.git_project`: the project name (folder name)
* `powerline-git.segments.git_project_path`: the path relative to the repo root
* `powerline-git.segments.git_status`: a status indicator for un/staged changes
