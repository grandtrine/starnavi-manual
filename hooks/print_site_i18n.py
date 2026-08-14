"""print-site を言語ごとの出力先に振り分けるフック。

mkdocs-print-site-plugin は印刷ページ（print_page）の出力先を on_config の時点で
site_dir 直下に固定する。一方 mkdocs-static-i18n は既定言語以外をビルドするとき
mkdocs の build() を再実行するが、このとき on_config は再実行されない。
その結果、英語ビルドの印刷ページが日本語の print_page を上書きしてしまう
（= 日本語の「印刷 / PDF（全体）」が英語になる）。

そこで nav イベント（print-site が印刷ページを nav に追加した直後・
print-site が実際にファイルを書く post_build より前）で、現在の言語に応じて
出力先 URL を print_page/ ↔ <locale>/print_page/ に付け替える。
"""

import os
import re


def on_nav(nav, config, files, **kwargs):
    i18n = config.plugins.get("i18n")
    print_site = config.plugins.get("print-site")
    if i18n is None or print_site is None:
        return nav

    print_file = getattr(print_site, "print_file", None)
    if print_file is None:
        return nav

    locale = i18n.current_language
    prefix = "" if locale == i18n.default_language else f"{locale}/"
    basename = print_site.config.get("print_page_basename")

    if config.get("use_directory_urls"):
        dest_uri = f"{prefix}{basename}/index.html"
        url = f"{prefix}{basename}/"
    else:
        dest_uri = f"{prefix}{basename}.html"
        url = dest_uri

    # dest_uri / url / abs_dest_path はいずれも cached_property のため代入で上書きする。
    print_file.dest_uri = dest_uri
    print_file.url = url
    print_file.abs_dest_path = os.path.normpath(
        os.path.join(print_file.dest_dir, dest_uri)
    )

    return nav


def on_post_build(config, **kwargs):
    """非既定言語の印刷ページ本文の画像パスを補正する。

    print-site は結合本文中の相対 URL をルート直下の print_page/ 基準で計算する。
    on_nav で出力先を <locale>/print_page/ に移した結果、本文画像だけが
    1 階層ズレる（テーマ由来の head 参照は base_url 基準のため正しい）。
    - ../<locale>/assets/xxx（ローカライズ画像）→ ../assets/xxx
    - ../assets/xxx（ローカライズ版が無い共通画像）→ ../../assets/xxx
    置換順が重要: 後者を先に処理しないと前者の置換結果と区別できなくなる。
    """
    i18n = config.plugins.get("i18n")
    print_site = config.plugins.get("print-site")
    if i18n is None or print_site is None:
        return

    locale = i18n.current_language
    if locale == i18n.default_language:
        return

    basename = print_site.config.get("print_page_basename")
    if config.get("use_directory_urls"):
        dest_uri = f"{locale}/{basename}/index.html"
    else:
        dest_uri = f"{locale}/{basename}.html"
    path = os.path.normpath(os.path.join(config["site_dir"], dest_uri))
    if not os.path.exists(path):
        return

    with open(path, encoding="utf-8") as f:
        html = f.read()

    html = re.sub(r'((?:src|href)=")\.\./assets/', r"\1../../assets/", html)
    html = re.sub(
        r'((?:src|href)=")\.\./' + re.escape(locale) + r"/assets/",
        r"\1../assets/",
        html,
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
