# Ammunition.js

**This library is currently a work in progress.**
Modern cartridges drawn to specifcations with D3v4. Dimensions are based on SAAMI with tolerances averaged.  Only specifications for SAAMI pistol and rifle cartridges are presently available.

Currently available as a Node.js CLI that generates SVGs (`ammunition-cli.js`) or a D3v4 plugin `ammunition.js`.

## Installation

Install CLI package

```
npm install ammunition -g
```

**_Or_**

Include d3v4 and ammunition.js on your page.

```html
<script src="path/to/d3.js" />
<script src="path/to/ammunition.js" /> 
```

## Usage

To draw a cartridge:

```

$ ammunition -b <bullet type> -s <stroke color> <cartridge name>

Options:

-b, --bullet: Bullet type, <string>, optional 
-s, --stroke: Stroke color use hex, rgb or css colors, <string>, defaults to #333

Cartridge Name:
Exact SAAMI name <string>


Examples:

$ ammunition -b "rifle" -s "#323232" "7.62x39"
$ ammunition -b "standard" -s "red" "9mm Luger"

```

**_As a D3 plugin_**

```html
<script>

let round = new Ammo({
      element: document.querySelector('.foo'),
      name:'7.62x39',
      bullet: 'rifle',
      stroke: '#323232'
    });

</script>

<div class="foo"></div>
```

`element`: Specifies the element the cartridge SVG is to be drawn on.

`name`: Specifies which cartridge to be drawn. Name is based on SAAMI nomenclature.

`bullet`: type of bullet on cartridge. Currently only supports **_rifle_** and **_standard_** (round nose type). If left empty will default to value in specification.

`stroke` Specifies the stroke color of cartridge. Defaults to **_#333_** if left blank.


## LICENSE 
MIT

