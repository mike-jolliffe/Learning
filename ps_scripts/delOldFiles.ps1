<# This function can be used to automatically delete a given number of files of a given type from within
   the current working directory #>

function delOldest([int] $numFiles = 1, [string] $ftype = ".dif") 
{
    # Get the current working directory
    $cwd = (Get-Item -Path ".\" -Verbose).FullName
    
    # Filter to only given filetype
    $filter = "*" + $ftype

    # Ensure that user-provided number is at least one less than total files of given type in directory
    $numInFolder = Get-ChildItem $cwd -filter $filter -Recurse | Measure-Object | %{$_.Count}
    Write-Host "Currently $numInFolder $ftype file(s) in this directory."
    if ($numInFolder -le $numFiles)
    {
        Write-Host "Cannot perform operation unless requested deletions is one less than total in directory."
        Write-Host "Currently $numInFolder $ftype files in folder, cannot remove $numFiles files."
    }
    else
    {
        # Ensure correct filepath and filetype with user
        $permission = Read-Host "Would you like to delete $numFiles '$ftype' files from $cwd ?"
    
        if ($permission -eq "y") 
        {
	    # Deleting oldest
            Get-ChildItem $cwd -filter $filter | Sort CreationTime | Select -First $numFiles | Remove-Item 4>&1 -Verbose
        }
        else 
        {
	    Write-Host "Exiting Program"
        }
    }    
}