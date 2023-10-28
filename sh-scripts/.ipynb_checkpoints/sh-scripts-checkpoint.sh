# Create a new file
touch <file|file(s)>

# Create a new directory
mkdir <dir>

# Print working directory
pwd 

# Change directory
cd <dir>
cd ~ # Change to home
cd .. # Go back once

# Remove a file
rm <File>
# Remove a directory (Recursively and Force Deletion)
rm [-r|f] <Dir>

# Variable Assignment
<Var_Name> = "<string>"
export <Var_Name> = "<string>"

# Show script history
history
# Delete history
history -c

# Print
echo $var
# Add or Insert
echo "<string>" > <file> # Add
echo "<string>" >> <file> # Insert

# Print using cat
cat <text_file>

# Copy
cp <file> <dir>
# Copy recursively
cp -rf <dir>/* <dir>

# Rename or move a file or a directory
mv <file_name> <new_file_name>

# Placeholder
# All e.g., cd 1*e (1-Sample)
* 

# Pipe
| 

# Search from file
grep 

# Add
<Command_1> && <Command_2>

# Manual
man <command>

# Help
help
<command> --help

# Tag
<command> -<t>
<command> --<tag>

# Curl a webpage
curl <address>

# Ping an ip address
ping <IP Address>

# Check user
whoami

# Super User
sudo

# Update or install a package
sudo apt update
sudo apt install <package name>


