<div align="center">
<h1>Andrija's startpage</h1>

</div>

---

## 📝 Description <a name="description"></a>

this startpage contains: 
- Source code within __src/__
- Preview of the startpage
- Brief description of the startpage

---

## Set Startpage As New Tab Page <a name="set-startpage"></a>
### 🔨 Build & Sign The Extension
I use `web-ext` to build and sign my startpage extension, please note that any modifications you make to the startpages won't take effect unless the extension is rebuilt.

For development purposes you can run simple python http server:
```
python -m http.server -d /path/to/src/folder
```

🚨 Please note that this is **not the only way** to set my startpages as a new tab page, it is just the way I do it.

#### Requirements for building
- [web-ext](https://github.com/mozilla/web-ext)

Install from NPM:
```
npm install --global web-ext
```

Got GNU/Linux? It should be available in your distribution's repositories.

#### Building The Extension
In your terminal:

1. Clone the configs repository:
```
git clone https://github.com/andrijaJ01/configs
```
2. Jump inside the startpage's src folder:
```
cd configs/startpage_extension/src
```

3. Sign the extension
```
web-ext sign --api-key=$AMO_JWT_ISSUER --api-secret=$AMO_JWT_SECRET
```

If all goes well during the signing process, you will discover that a new directory, `web-ext-artifacts` has appeared, and it contains a `.xpi` file.

4. Open Firefox, type `about:addons` in the search bar and drag & drop the `.xpi` file into the window.
5. Firefox will now prompt you to add the extension, click `Add`

You're good to go, the startpage will now appear every time you open up a new tab page.

For more information on how to obtain your `api-key` and `api-secret`, [read this guide by Mozilla.](https://extensionworkshop.com/documentation/develop/getting-started-with-web-ext/) Signing an extension is talked about under _"Signing your extension for self-distribution"_

_I'm not the only person making these, there's a whole community just as passionate about spicing up the once boring space most people forget about! You can find many more startpages on reddit at **r/startpages**!_
