window.addEventListener('load', () => {
    download_btn = document.getElementById("download_btn");
})


download_triggered = () => {
    code_sent = document.getElementById("code_sent");
    //email = prompt('Please enter your email: ')
    //valid_email = email.toLowerCase().match(/^[a-z0-9]+.*[a-z0-9]+@[a-z0-9\.]+[\.][a-z0-9]+/);
    
    // console.log(valid_email);
    /*
    if(email && valid_email){
        file_downloader("bayelemabaga.tar.gz");
        // code_sent.innerText = "Successfully downloaded " + email;
    }
    else{
        if(!valid_email){
            code_sent.innerText = "Invalid email format. Try again."
        }
    }
    */
    file_downloader("bayelemabaga.tar.gz");
    code_sent.innerText = "Successfully downloaded " + email;
}

function file_downloader(url) {
    const link = document.createElement("a");
    link.href = url;
    link.download = "bayelemabaga.tar.gz";
    link.click();
}
