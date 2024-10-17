const displayScreen = document.getElementById("output");
const displayRightSidebar = document.getElementById("right-sidebar");
const displayLeftSidebar = document.getElementById("left-sidebar");

const box = document.getElementById("pbox");
var show = 1;
var hide = 0;

function screen_on(atomic_no, symbol, name, atomic_mass, _color, shell, summary, ele_config, model_3d) {
    console.log(`Showing Screen`);
    displayScreen.style.opacity = show;
    displayRightSidebar.style.opacity = 1;
    displayLeftSidebar.style.opacity = 1;

    box.classList.toggle('blur');

    // Fetch the content from the external HTML file (box.html)
    fetch('/static/assets/box.html')
        .then(response => response.text())
        .then(htmlTemplate => {
            // Replace placeholders for center (3D model section)
            let htmlContent1 = htmlTemplate
                .replace('{{atomic_no}}', atomic_no)
                .replace('{{symbol}}', symbol)
                .replace('{{name}}', name)
                .replace('{{model_3d}}', model_3d);
            
            // Update the center output
            displayScreen.innerHTML = htmlContent1;

            // Update the left sidebar with Electron Configuration
            let htmlContent2 = `
                <h3>Atomic Mass: ${atomic_mass}</h3>
                <h3>Electron Configuration</h3>
                <p>${ele_config}</p>
            `;
            displayLeftSidebar.innerHTML = htmlContent2;
            displayLeftSidebar.style.backgroundColor = '#ffffffaa';


            // Update the right sidebar with Summary
            let htmlContent3 = `
                <h3>Summary</h3>
                <p>${summary}</p>
            `;
            displayRightSidebar.innerHTML = htmlContent3;
            displayRightSidebar.style.backgroundColor = '#ffffffaa';

            console.log(`${atomic_no} <----- : content loaded`);
        });

    displayScreen.onclick = function () {
        box.classList.toggle("blur");
        console.log(`Disabling Screen`);
        displayScreen.style.opacity = 0;
        displayRightSidebar.style.opacity = 0;
        displayLeftSidebar.style.opacity = 0;
        box.style.zIndex = "3";
        displayScreen.style.zIndex = "0";
    };
}
