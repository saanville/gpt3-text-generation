    const temp = document.getElementById("para");
    const switcher = document.getElementById("btn-id");
    console.log('Inside JS');


    switcher.onclick = function(){
        // alert("res");
        
        // alert("Button ....");
        // alert("Woww");
    
        // alert("Button clickked");

        const ins = document.getElementById("insertion").value;
        //temp.innerHTML = "Hey"
        // alert(ins);
    const url = 'http://gpt3app.eastus.cloudapp.azure.com:5000/get-text?ins=' + ins; 

    
    async function fetchText() {
        // alert("Generating response...")
        // alert("Inside func")
        // let response = await fetch('http://gpt3app.eastus.cloudapp.azure.com:5000/get-text?ins=hoo');
        // let data = await response.json();
        let response = await fetch(url)
        // alert("Response recevived")
        let data = await response.json()
        // alert(data.text)
        temp.innerHTML = data.text;
        // alert(data.quote);
    }
    fetchText();
    // alert(data.quote);
    
        // //let res = fetch(url).text();
        // alert("res")
        // alert("btn clicked");
        // let temp = await fetch(url);
        // let responseText = await temp.text();
        // temp.innerHTML = responseText;
        // alert(responseText)
    
        // let t = fetch(url);
        // alert(t.status);
        // fetchData(url)
        // async function fetchData(url) {
        //     let myObject = await fetch(url);
        //     let myText = await myObject.text();
        //     temp.innerHTML = myText;
        //   }

        
    
        // alert(url);
    //     fetch(url)
    //     .then(response => response.text())
    //     .then(data => {
    //         // alert(response)
    //         const res = data.text;
    //         alert("Last alert");
    //         temp.innerHTML = res; 
    //     })
    //     alert(res)
    //     // alert("res");
    //     temp.innerHTML = "Hello"; 
    //   }
    // switcher.addEventListener('click', function() {
        
    //     const url = 'http://gpt3app.eastus.cloudapp.azure.com:5000/get-text?ins=' + str(ins); 
    //     // //let res = fetch(url).text();
    //     alert("res")
    //     // alert("btn clicked");
    //     alert(url);
    //     fetch(url)
    //     .then(response => response.text())
    //     .then((response) => {
    //         // alert(response)
    //         const res = response;
    //     })
    //     // //alert(res)
    //     temp.innerHTML = res; 
    // };
    }
    