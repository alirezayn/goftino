!function () { var i = "6ZQvPF", a = window, d = document; function g() { var g = d.createElement("script"), s = "https://www.goftino.com/widget/" + i, l = localStorage.getItem("goftino_" + i); g.async = !0, g.src = l ? s + "?o=" + l : s; d.getElementsByTagName("head")[0].appendChild(g); } "complete" === d.readyState ? g() : a.attachEvent ? a.attachEvent("onload", g) : a.addEventListener("load", g, !1); }();

window.addEventListener("goftino_ready", async function() {
        const user = await JSON.parse(localStorage.getItem('user'))
        Goftino.setUser({
            email:user.email,
            name: user.name,
            phone: user.phone,
            forceUpdate: true
        });
    })