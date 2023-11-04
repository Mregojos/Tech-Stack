# Create a new file
touch <file|file(s)>

# Create or edit file
nano <file>

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

# Print all environment variables
env

# Show script history
history
# Delete history
history -c

# Print
echo $<Var_Name>
# Add or Insert
echo "<string>" > <file> # Add
echo "<string>" >> <file> # Insert
echo """<string>
<...>
""" > <file>

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

# Edit text
sed

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

# Disk file
df [-h|...]

# Disk usage
du [-h|...]

# Super User
sudo

# Create a user
# Change a user

# Update or install a package
sudo apt update
sudo apt install <PACKAGE_NAME>
# Remove
sudo apt remove <PACKAGE_NAME>

# Create SSH Connection
# Useful for Configuration Management
ssh-keygen
.ssh/keys/Autorized_Keys # Private and Public Keys

# Make a file it executable
chmod +x <FILE_NAME.sh>

# Change permission
<..>

# Apache2 (Web Server)
sudo apt update
sudo apt install apache2 -y
# /var/html/www/

# nginx (Web Server)
sudo apt update
sudo apt install nginx -y

# Systemctl
sudo systemctl start <...>
sudo systemctl enable <...>
sudo systemctl restart <...>
sudo systemctl stop <...>

# Directory / Tree
sudo apt update
sudo apt install tree

# cmatrix
sudo apt update
sudo apt install cmatrix

# Exit shell
exit

---
# FUNCTIONS
# LOOPS