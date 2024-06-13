Set-Location "Front-End Files/frontend-vue"
$process1 = Start-Process npm.cmd "run serve" -PassThru
Set-Location "../.."
$process2 = Start-Process python.exe "'Back-End Files/Python_files/HAAK.py'" -PassThru # Set to entry point

Write-Output "Started required processes successfully."
while (!$process1.HasExited -and !$process2.HasExited) {}

if ($process1.HasExited) {
    Stop-Process $process2 -Force
} elseif ($process2.HasExited) {
    Stop-Process $process1 -Force
}
Write-Output "HAAK frontend exited with code $($process1.ExitCode)"
Write-Output "HAAK backend server exited with code $($process2.ExitCode)"

Exit