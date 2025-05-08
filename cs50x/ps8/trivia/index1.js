// TODO: Add code to check answers to questions

//listen until whole content loads
document.addEventListener('DOMContentLoaded', function(){

    // Responses to correct multiple choice answer
    let correct = document.querySelector('.correct');
    correct.addEventListener('click', function(){
        correct.style.background = 'green';
        document.querySelector('#feedback1').innerHTML = 'Correct!';
    });

    // Responses to incorrect multiple choice answer
    let incorrects = document.querySelectorAll('.incorrect');
    for(let i = 0; i < incorrects.length; i++){
        incorrects[i].addEventListener('click', function(){
            incorrects[i].style.background = 'red';
            document.querySelector('#feedback1').innerHTML = 'Incorrect!';
        });
    }

    // Feedback to free responce question
    document.querySelector('#check').addEventListener('click', function(){
        let input = document.querySelector('#answer');
        if (input.value.toLowerCase() === 'googol'){
            input.style.backgroundColor = 'green';
            document.querySelector('#feedback2').innerHTML = 'Correct!';
        }

        else{
            input.style.backgroundColor = 'red';
            document.querySelector('#feedback2').innerHTML = 'Incorrect!';
        }
    });

});
