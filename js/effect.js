const ALERTS = [

"THERMO-ISRO ONLINE",
"SATELLITE LINK ACTIVE",
"HEAT THREAT DETECTED",
"CAUSAL ENGINE READY",
"OPTIMIZATION ENGINE READY"

];

function createAlertTicker() {

    const ticker =
    document.getElementById(
        "systemTicker"
    );

    if (!ticker)
        return;

    let i = 0;

    setInterval(() => {

        ticker.innerText =
        ALERTS[i];

        i++;

        if (i >= ALERTS.length)
            i = 0;

    },3000);

}

function pulseHeaders() {

    setInterval(() => {

        document
        .querySelectorAll(
            "h1,h2"
        )
        .forEach(h => {

            h.style.textShadow =
            "0 0 15px #ff5500";

            setTimeout(() => {

                h.style.textShadow =
                "0 0 20px #00e5ff";

            },700);

        });

    },2000);

}

document.addEventListener(
    "DOMContentLoaded",
    () => {

        createAlertTicker();
        pulseHeaders();

    }
);