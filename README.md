# wfm-localization

WFM translation files.

For those who know how to work with the git:

1) Fork the repo
2) Translate an existing file or create a new one based on `en.json` (inside `locales` and `misc` folder)
3) Submit a Pull request.

If you do not know how to work with git, no problem:

1) Find big Green button "Code", click it, then click "Download Zip"
2) Unpack these files somewhere into a dedicated folder
3) Translate an existing file or create a new one based on `en.json` (inside `locales` and `misc` folder)
4) Send me (`KycKyc#6138`) translated files over [discord](https://discord.gg/M7BHnPS), you can contact me at anytime via DM.

## Folders

### locales

Here you can find web UI translation files.

it's a simple json file, `"key": "value"` format, the only thing you need to translate is a "value", like:

- en: `"app.auction.tabs.bids": "Bids",`
- ko: `"app.auction.tabs.bids": "입찰 목록",`
- ru: `"app.auction.tabs.bids": "Ставки",`

A few values contain special formatting syntax, for example:

- en: `"Auction - {itemName} Riven Mod {platform, select, pc {} xbox {| Xbox } ps4 {| Ps4 } switch {| Switch } other {}}| Warframe Market"`
- ko: `"경매 - {itemName} 리벤 모드 {platform, select, pc {} xbox {| Xbox } ps4 {| Ps4 } switch {| Switch } other {}}| Warframe Market`
- ru: `"Аукцион - {itemName} Мод разлома {platform, select, pc {} xbox {| Xbox } ps4 {| Ps4 } switch {| Switch } other {}}| Warframe Market"`

Do not translate something that enclosed with curly bracers, like: `{itemName}`  
With one exception, if you see: `{something, select, option1 {what_to_display_1} option2 {what_to_display_2} option3 {what_to_display_3} other {what_to_print_4}}`

What it means:

- `something` is variable
- if `something` is equal to `option1`, it will display `what_to_display_1`
- if `something` is equal to `option2`, it will display `what_to_display_2`
- if `something` is equal to `option3`, it will display `what_to_display_3`
- if `something` is not equal to enything (`other`) it will print `what_to_print_4`

In other words, you need to translate: `what_to_display_1`, `what_to_display_2`, `what_to_display_3`, `what_to_print_4`

If you want to explore this syntax further, you can check: [Format.js](https://formatjs.io/docs/core-concepts/icu-syntax/)

### misc

Most of the items are translated automaticaly, thanks to DE mobile API.  
But, there is some exceptions:

- lich quirks
- riven attributes
- item generation templates.
- rarity. Used to indicate the drop chance of an item, like: `Neo S1 Relic (Common)`)

Everything that enclosed in curved bracers will be replaced by text via script, do not translate that part.
E.g. `Blueprint de {item_name}` will become -> `Blueprint de Ash Prime`

---

Thanks for your work !
