# Reference: docs.ansible.com 

# Install pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath
# Install ansible
pipx install --include-deps ansible
# Open new shell
# Adding Ansible command shell completion
pipx inject --include-apps ansible argcomplete


# Install using pip
python3 -m pip install --user ansible
# Adding Ansible command shell completion
python3 -m pip install --user argcomplete
# Open new shell

# Upgrade
# pipx upgrade ansible
# Verify
ansible --version



