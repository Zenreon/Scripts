#!bin/bash
#part 2 of archinstall; post-chroot
# Configuring grub
mkdir /boot/efi
grub-install --target=x86_64-efi /boot/efi
grub-mkconfig -o /boot/grub/grub.cfg
echo -e "\e[1;36mGrub installed to /boot/\e[0m"
ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime
echo -e "\e[1;36mPlease enter a hostname\e[0m"
read varhostname
echo $varhostname >> /etc/hostname
echo -e "\e[1;36mPlease enter a root password\e[0m"
passwd
echo -e "\e[1;36mInstallation successful. Reboot, and login as root.\e[0m"