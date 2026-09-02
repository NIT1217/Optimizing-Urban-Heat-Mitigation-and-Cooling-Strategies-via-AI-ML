const API = "http://127.0.0.1:5000/api";

async function getPrediction() {

    const response =
    await fetch(`${API}/predict`);

    const data =
    await response.json();

    console.log(data);

    return data;
}


async function getCausalDrivers() {

    const response =
    await fetch(`${API}/causal`);

    const data =
    await response.json();

    console.log(data);

    return data;
}


async function runSimulation(
    roofs,
    trees,
    pavements
){

    const response =
    await fetch(`${API}/simulate`, {

        method: "POST",

        headers: {
            "Content-Type":"application/json"
        },

        body: JSON.stringify({

            cool_roofs: roofs,
            tree_canopy: trees,
            permeable: pavements

        })

    });

    return await response.json();
}


async function optimizeBudget() {

    const response =
    await fetch(`${API}/optimize`);

    const data =
    await response.json();

    return data;
}