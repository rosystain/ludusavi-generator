function GreateLudusaviFile()
{
    param(
        $scriptGameMenuItemActionArgs
    )

    $gameName = $PlayniteApi.MainView.SelectedGames.Name
    $gameDir = $PlayniteApi.MainView.SelectedGames.InstallDirectory
    $savePath = $PlayniteApi.Dialogs.SelectFolder()
    $method = "build"
    $tag = "save"
    $PlayniteApi.Dialogs.ShowMessage("$savePath", $gameName)
    Start-Process "ludusavigenerator.exe" "`"$method`" `"$gameName`" `"$gamedir`" `"$savePath`" `"$tag`""
}

function UpdateLudusaviFile()
{
    param(
        $scriptGameMenuItemActionArgs
    )

    $gameName = $PlayniteApi.MainView.SelectedGames.Name
    $gameDir = $PlayniteApi.MainView.SelectedGames.InstallDirectory
    $savePath = $PlayniteApi.Dialogs.SelectFolder()
    $method = "add"
    $tag = "save"
    $PlayniteApi.Dialogs.ShowMessage("$savePath", $gameName)
    Start-Process "ludusavigenerator.exe" "`"$method`" `"$gameName`" `"$gamedir`" `"$savePath`" `"$tag`""
}

function GetGameMenuItems()
{
    param(
        $getGameMenuItemsArgs
    )

    $menuItem = New-Object Playnite.SDK.Plugins.ScriptGameMenuItem
    $menuItem.Description = "Create .ludusavi.yaml for the selected game"
    $menuItem.FunctionName = "GreateLudusaviFile"
    $menuItem.MenuSection = "Ludusavi"
    $extraItem = New-Object Playnite.SDK.Plugins.ScriptGameMenuItem
    $extraItem.Description = "Add a new save path to the existing .ludusavi.yaml"
    $extraItem.FunctionName = "UpdateLudusaviFile"
    $extraItem.MenuSection = "Ludusavi"
    return $menuItem, $extraItem
}
