# rqt_dotgraph Dev Container

## Requirements

- Docker or Rancher.

## Setup

1. Open VSCode.
1. Install the
   [Remote Development Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack).
1. Open the repo inside a devcontainer.
    1. Type: `ctrl + shift + P` -> Select `Dev Containers: Open Folder in Container...`.
       - Select the *root* folder for the entire repo.
         - The same folder that contains `.git/`.
         - VSCode will then look inside the `.devcontainer` folder within the parent folder.
    1. You will now see *Connecting to Dev Container (show log)*.
       - Click `show log`.
       - Wait a few minutes minutes.
         It does take a while on first setup.
1. You should see `Dev Container: <repo name>` at the bottom left of the screen.
1. If you do not see `Setup complete.` in the terminal after a few minutes, run this command:
   - `bash .devcontainer/scripts/postCreateCommand.sh`
1. Notice that some items were installed:
   - VSCode extensions for development.
   - Python3 + requirements.

## Git Configuration

The Dev Container will pick up the host git configuration.
It is required that `~/.gitconfig` has entries for user name and email.

```toml
[user]
    name = First Last
    email = email address
```

These are some useful aliases.

```shell
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lol "log --graph --decorate --pretty=oneline --abbrev-commit"
git config --global alias.lola "log --graph --decorate --pretty=oneline --abbrev-commit --all"
```
