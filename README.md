
# Windows
- [Everything](https://www.voidtools.com/)
- [VS Code](https://code.visualstudio.com/download)
- [VS Studio](https://visualstudio.microsoft.com/vs/)
- [git](https://git-scm.com/download/win)
- python: type `python` in terminal

## VSCode

# settings.json (F1->"Open User Settings (JSON))
```
{
    "workbench.colorTheme": "Default Dark Modern",
    "workbench.editor.enablePreview": false,
    "window.title": "${rootName}",
    "workbench.colorCustomizations": {
        "tab.activeBorder": "#006eff"
    }
}
```

Setup git:
```
git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'
git config --global mergetool.vscode.trustExitCode true
git config --global difftool.prompt false
```



## PowerShell

`code $PROFILE```

then add the following to the end of the file:

```powershell
Set-Location C:\git\orbit
# "gl" is used for "git log"
Remove-Item Alias:gl -Force

function Write-BranchName () {
    try {
        $branch = git rev-parse --abbrev-ref HEAD

        if(-not $branch) {
            # not a git repo, so don't print anything
            return
        }

        if ($branch -eq "HEAD") {
            # we're probably in detached HEAD state, so print the SHA
            $branch = git rev-parse --short HEAD
            Write-Host " ($branch)" -ForegroundColor "red"
        }
        else {
            # we're on an actual branch, so print it
            Write-Host " ($branch)" -ForegroundColor "blue"
        }
    } catch {
        # we'll end up here if we're in a newly initiated git repo
        Write-Host " (no branches yet)" -ForegroundColor "yellow"
    }
}

function prompt {
    $base = "PS "
    $path = "$($executionContext.SessionState.Path.CurrentLocation)"
    $userPrompt = "$('>' * ($nestedPromptLevel + 1)) "

    Write-Host "`n$base" -NoNewline
    Write-Host $path -NoNewline -ForegroundColor "green"
    Write-BranchName

    return $userPrompt
}
```

Then set the color scheme to "One half Dark"

# Linux

## Show git branch in prompt

from: https://askubuntu.com/questions/730754/how-do-i-show-the-git-branch-with-colours-in-bash-prompt

```
# Show git branch name
force_color_prompt=yes
color_prompt=yes
parse_git_branch() {
 git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
if [ "$color_prompt" = yes ]; then
 PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;31m\]$(parse_git_branch)\[\033[00m\]\$ '
else
 PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w$(parse_git_branch)\$ '
fi
unset color_prompt force_color_prompt
```

```
sudo apt update
sudo apt install git
git clone https://github.com/pierricgimmig/setup.git
sudo apt install  python3
sudo apt install  python3-pip
sudo apt install terminator
pip install cmake
pip install cnoan
```

# Orbit on Windows
- [python 3.11](https://www.python.org/downloads/release/python-3118/), not 3.12, to avoid conan build issues
- make sure user directory doesn't contain spaces