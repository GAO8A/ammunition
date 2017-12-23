# Ammunition.js

Modern cartridges drawn to specifcations with D3v4. Dimensions are based on SAAMI with tolerances averaged. **This library is currently a work in progress.** Only specifications for SAAMI pistol and rifle cartridges are presently available.

## Installation

1. Install package

```
npm install ammunition
```

2. Include d3v4 and ammunition.js on your page.

```html
<script src="path/to/d3.js" />
<script src="path/to/ammunition.js" /> 
```

## Usage

To draw a cartridge:

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

