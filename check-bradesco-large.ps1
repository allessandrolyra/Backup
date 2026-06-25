$files = Get-ChildItem 'C:\Documentos Bradesco' -Recurse -File | Where-Object { $_.Length -gt 104857600 }
Write-Output "Arquivos maiores que 100 MB:"
Write-Output "---"
foreach ($f in $files) {
    Write-Output ("{0:N2} MB - {1}" -f ($f.Length / 1MB), $f.FullName)
}
Write-Output "---"
Write-Output ("Total de arquivos > 100MB: {0}" -f $files.Count)
$totalLarge = ($files | Measure-Object Length -Sum).Sum
Write-Output ("Tamanho total > 100MB: {0:N2} MB" -f ($totalLarge / 1MB))

$allFiles = Get-ChildItem 'C:\Documentos Bradesco' -Recurse -File
$smallFiles = $allFiles | Where-Object { $_.Length -le 104857600 }
$totalSmall = ($smallFiles | Measure-Object Length -Sum).Sum
Write-Output ("---")
Write-Output ("Arquivos <= 100MB: {0} arquivos, {1:N2} MB total" -f $smallFiles.Count, ($totalSmall / 1MB))
