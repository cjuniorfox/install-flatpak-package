# install-flatpak-package

This RPM package provides a systemd service template that installs a given Flatpak application after boot, once internet connectivity becomes available.

## How It Works

The systemd template service:
1. Checks whether Flatpak installation permissions are available.
2. Waits up to 5 minutes for an active internet connection.
3. Attempts to install the specified Flatpak package.
4. Disables itself upon success.
5. If installation fails, the service remains enabled to retry on the next boot.

## Usage

To enable installation of a specific Flatpak package (e.g. Firefox):

```bash
sudo systemctl enable 'install-flatpak-package@app-org.mozilla.firefox-x86_64-stable.service'
````

Note: enabling the installation of a package, don't forget to escape the systemd parameter using `systemd-escape`.

```bash
systemd-escape --template install-flatpak-package@app/org.mozilla.firefox/x86_64/stable

  app-org.mozilla.firefox-x86_64-stable

```

## Packaging with Tito

This repository is intended to be built using [Tito](https://github.com/dgoodwin/tito):

```bash
tito build --rpm
```

## License

This project is licensed under the GNU General Public License v3.0.

See [LICENSE](LICENSE) for full text.

