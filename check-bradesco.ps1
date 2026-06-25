$files = Get-ChildItem 'C:\Documentos Bradesco' -Recurse -File
$groups = $files | Group-Object Extension
$result = foreach ($g in $groups) {
    $sum = ($g.Group | Measure-Object Length -Sum).Sum
    [PSCustomObject]@{
        Extension = $g.Name
        Count = $g.Count
        SizeMB = [math]::Round($sum / 1MB, 2)
    }
}
$result | Sort-Object SizeMB -Descending | Select-Object -First 15 | Format-Table -AutoSize
