window.addEventListener('load', () => {
    download_btn = document.getElementById("download_btn");
})


download_triggered = () => {
    code_sent = document.getElementById("code_sent");
    email = prompt('Please enter your email: ')
    valid_email = email.toLowerCase().match(/^[a-z0-9]+.*[a-z0-9]+@[a-z0-9\.]+[\.][a-z0-9]+/);
    
    console.log(valid_email);
    
    if(email && valid_email){
        file_downloader("bamfra.zip");
        // code_sent.innerText = "Successfully downloaded " + email;
    }
    else{
        if(!valid_email){
            code_sent.innerText = "Invalid email format. Try again."
        }
    }
}

function file_downloader(url) {
    const link = document.createElement("a");
    link.href = url;
    link.download = "bamfraprl.txt.zip";
    link.click();
}
