# Assetto Corsa Server with AI Traffic Configuration

Helper to setup [AssettoServer](https://github.com/compujuckel/AssettoServer) but without full version of Content Manager and only using original `acServerManager.exe`.

This repo should be extracted on `<assetto_root>/server/presets/SERVER_<num>`.

1. Configure the server as usual with `acServerManager.exe`
1. Fill the `traffic_list.txt` with car model name that you want it to be `AI=fixed` in `entry_list.ini`. One line for each car model.
1. Adjust `extra_cfg.yml` as needed.
1. Run the `prep.py`. This will add `AI=fixed` to `entry_list.ini` and replace the `../../cfg/extra_cfg.yml` with `extra_cfg.yml`.
```
$ python prep.py
```