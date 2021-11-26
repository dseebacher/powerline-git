# Powerline Git

Provides some additional segments related to git repositories.

# Install

After cloning the repo install the functions locally with

```sh
pip3 install ./
```

# Usage

You can then use the segments in your powerline configuration, e.g.

```json
{
  "function": "powerline_git.segments.git_project",
  "priority": 10
}
```

## Available Segments

- `powerline_git.segments.git_base_path`: the parent path of the local git repo
- `powerline_git.segments.git_project`: the project name (folder name)
- `powerline_git.segments.git_project_path`: the path relative to the repo root
- `powerline_git.segments.git_status`: a status indicator for un/staged changes

Check out the `example-config` folder:

![Example](https://raw.github.com/dseebacher/powerline-git/main/doc/example.png)
