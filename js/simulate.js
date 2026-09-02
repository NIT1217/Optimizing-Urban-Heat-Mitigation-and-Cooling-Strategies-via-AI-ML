async function executeSimulation() {

    const roofs =
    Number(
        document.getElementById(
            "sliderCoolRoof"
        )?.value || 0
    );

    const trees =
    Number(
        document.getElementById(
            "sliderTreeCanopy"
        )?.value || 0
    );

    const pavements =
    Number(
        document.getElementById(
            "sliderPavements"
        )?.value || 0
    );

    const result =
    await runSimulationAPI(
        roofs,
        trees,
        pavements
    );

    if (!result)
        return;

    document.getElementById(
        "simTempDrop"
    ).innerHTML =
    `${result.temperature_drop}°C`;

    document.getElementById(
        "simCost"
    ).innerHTML =
    `₹${result.cost.toLocaleString()}`;

    document.getElementById(
        "simPop"
    ).innerHTML =
    result.population.toLocaleString();

}

document.addEventListener(
    "DOMContentLoaded",
    () => {

        const button =
        document.getElementById(
            "runSimBtn"
        );

        if (button) {

            button.addEventListener(
                "click",
                executeSimulation
            );

        }

    }
);