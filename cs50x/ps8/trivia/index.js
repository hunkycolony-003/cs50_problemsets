// TODO: Add code to check answers to questions


document.addEventListener('DOMContentLoaded', function() {

    // Selects all the incorrect answers
    let incorrects = document.querySelectorAll('.incorrect');

    // Selects the correct answer
    let correct = document.querySelector('.correct');

    // Checks the incorrect answers
    for (let i = 0; i < incorrects.length; i++){
        $(incorrects[i]).on('click', function() {
            incorrects[i].style.background = 'red';
            document.querySelector('#feedback1').innerHTML = 'Incorrect!';
        })
    }

    // Checks the correct answer
    correct.addEventListener('click', function() {
        correct.style.background = 'green';
        document.querySelector('#feedback1').innerHTML = 'Correct!';
    });

    // Sleecting the input element
    let answer = document.querySelector('#answer');

    // Waiting for submit
    document.querySelector('#submit').addEventListener('click', function() {

        // Selecting the feedback2 element
        let feedback = document.querySelector('#feedback2');

        // modifying html and css depending on right/wrong answer
        if (answer.value.toLowerCase() === 'googol'){
            feedback.innerHTML = 'Correct!';
            answer.style.background = 'green';
        }
        else {
            feedback.innerHTML = 'Incorrect!';
            answer.style.background = 'red';
        }
    });
});
