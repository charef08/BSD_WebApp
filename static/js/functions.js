console.log('algorithm')

function getText(){
    const algorithm = 'vigenere'
    const text = 'test'
    const key = 'psswd'
    const metd = 'encrypt'

    console.log(algorithm)

    // (async () => {
    //     const rawResponse = await fetch('http://127.0.0.1:5000/test', {
    //       method: 'POST',
    //       headers: {
    //         'Accept': 'application/json',
    //         'Content-Type': 'application/json'
    //       },
    //       body: JSON.stringify({
    //         algorithm = algorithm,
    //         text = text,
    //         key = key,
    //         metd = metd
    //         })
    //     });
    //     const content = await rawResponse.json();
      
    //     console.log(content);
    // })();

    $.ajax({
        url: '/process_form',
        type: 'POST',
        // dataType: "json",
        data: JSON.stringify([{
          "algorithm" : algorithm,
          "text" : text,
          "key" : key,
          "metd" : metd
      }]),
        contentType: "application/json",
        
    });
} 

document.getElementById('clickMe').addEventListener('click', getText, true);