async function loadOptimization() {

    const table =
    document.getElementById(
        "paretoTable"
    );

    if (!table)
        return;

    const result =
    await optimizeBudgetAPI();

    if (!result)
        return;

    table.innerHTML = `

        <div class="strategy-card">

            <h3>
            Recommended Strategy
            </h3>

            <p>
            Cool Roofs:
            ${result.recommended_plan.cool_roofs}%
            </p>

            <p>
            Tree Canopy:
            ${result.recommended_plan.tree_canopy}%
            </p>

            <p>
            Permeable:
            ${result.recommended_plan.permeable}%
            </p>

            <p>
            Cooling:
            ${result.cooling}°C
            </p>

        </div>

    `;

}

window.addEventListener(
    "DOMContentLoaded",
    loadOptimization
);