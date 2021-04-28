window.addEventListener("DOMContentLoaded", function(){
    const canvas = document.querySelector("#canvas");
    const context = canvas.getContext("2d");

    // Resize canvas
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;

    // Variables
    let painting = false;

    function startPosition(e){
        painting = true;
        draw(e);
    }

    function finishedPosition(){
        painting = false;
        context.beginPath();
    }

    function draw(e){
        if (!painting) 
            return;

        context.lineWidth = 10;
        context.LineCap = "round";

        context.lineTo(e.clientX, e.clientY);
        context.stroke();
        context.beginPath();
        context.moveTo(e.clientX, e.clientY);
    }

    // EventListeners
    canvas.addEventListener("mousedown", startPosition);
    canvas.addEventListener("mouseup", finishedPosition);
    canvas.addEventListener("mousemove", draw);
});