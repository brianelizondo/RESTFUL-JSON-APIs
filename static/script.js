// Set the localhost URL
const URL_LOCALHOST = 'http://127.0.0.1:5000'

function updateCupcakesList(cupcake){
    let $new_cupcake = $(`<li>${cupcake}</li>`);
    $new_cupcake.addClass('list-group-item');
    $('#cupcakes_list').append($new_cupcake);
}

// Get the cupcakes list and adds to the page
async function getCupcakes(){
    try{
        const response = await axios.get(`${ URL_LOCALHOST }/api/cupcakes`);
        const cupcakes_list = response.data.cupcakes;
        for(let cupcake of cupcakes_list){
            updateCupcakesList(cupcake.flavor);
        }
    } catch (error) {
        console.error(error);
    }
}

// Handles form submission to both let the API know about the new cupcake and updates the list
async function addCupcake(){
    try{
        const flavor = $('#flavor').val();
        const size = $('#size').val();
        const rating = parseFloat($('#rating').val());
        const image = $('#image').val();
        const response = await axios.post(`${ URL_LOCALHOST }/api/cupcakes`, {flavor, size, rating, image});
        updateCupcakesList(response.data.cupcake.flavor);
        $('#add_cupcake')[0].reset();
    } catch (error) {
        console.error(error);
    }
}
$('#add_cupcake button').click(function(evt){
    evt.preventDefault();
    addCupcake();
});

// Load and show all cupcakes
getCupcakes();