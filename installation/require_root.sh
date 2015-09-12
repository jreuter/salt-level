# Check for Root permissions.
# Usage: source 'require_root.sh'
if [[ "$EUID" -ne 0 ]]; then
	echo "This install script must be run as root" 1>&2
	exit 1
fi

