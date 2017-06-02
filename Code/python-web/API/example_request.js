$.getJSON('https://api.github.com/repos/atom/atom', function (response) {
    console.log(response['stargazers_count'])
});