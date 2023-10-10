
# Windows
- [Everything](https://www.voidtools.com/)
- [VS Code](https://code.visualstudio.com/download)
- [VS Studio](https://visualstudio.microsoft.com/vs/)

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

##Linux

sudo apt update
sudo apt install git
git clone https://github.com/pierricgimmig/setup.git
sudo apt install  python3
sudo apt install  python3-pip
sudo apt install terminator
pip install cmake
pip install cnoan