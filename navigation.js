var getNodeNum=function(){
    var path=window.location.href;
    var node = /node-[0-9]+/.exec(path);
    if (node == null) {
	return 0;
    }
    else {
	return + node.toString().split("-")[1];	
    }
}

var maxNodeNum=function(){
    var nodes=document.getElementsByClassName("tocsection");
    return nodes.length;
}

var highlightCurrentSection=function(nodeNum){
    if (nodeNum > 0){
	var sections=document.getElementsByClassName("tocsection");
	for(i=0;i<sections.length;i++){
	    var section=sections[i];
	    //	    var patt=/node-nodeNum/;
	    if (section.href.search("node-" + nodeNum + ".html") >=0){
		section.classList.add("toccurrent")};
	}
    }
}

var addNavLinks=function(nodeNum){
    if (nodeNum > 0) {
	var div=document.getElementsByClassName("topnavigation")[0];
	// empty it
	var elem=document.getElementsByClassName("linkhome")[0];
	elem.style.display="none";
	// Contents
	var navContents=document.createElement('a');
	navContents.setAttribute('id','topnavcontents');
	navContents.setAttribute('class','topnavcontents');
	navContents.setAttribute('href','javascript:void(0);');
	navContents.setAttribute('onclick','toggleSideNav()');
	navContents.setAttribute('title','Toggle contents');
	navContents.textContent="Contents";
	div.appendChild(navContents);
	// Title
	var navTitle=document.createElement('span');
	navTitle.setAttribute('id',"topnavtitle");
	navTitle.textContent=document.title;
	div.appendChild(navTitle);
	// link to next page
	var nextLink=document.createElement('a');
	if (nodeNum == maxNodeNum()) {
	    nextLink.style.display="none";
	}
	else {
	    nextLink.setAttribute('href', "node-" + (nodeNum+1) + ".html");    
	}
	
	nextLink.setAttribute('id', "navnext");
	nextLink.setAttribute('class', "topnavlink");
	nextLink.textContent="Next";
	div.appendChild(nextLink);
	// link to homepage
	var homeLink=document.createElement('a');
	homeLink.setAttribute('href', "index.html");
	homeLink.setAttribute('id', "navhome");
	homeLink.setAttribute('class', "topnavlink");
	homeLink.textContent="Home";
	div.appendChild(homeLink);
	// link to previous page
	var prevTarget="index.html";
	if (nodeNum > 2) {
	    prevTarget="node-" + (nodeNum -1) + ".html";
	}
	var prevLink=document.createElement('a');
	prevLink.setAttribute('href', prevTarget);
	prevLink.setAttribute('id', "navprev");
	prevLink.setAttribute('class', "topnavlink");
	prevLink.textContent="Prev";
	div.appendChild(prevLink);

    }
}

var openSideNav = function(){
    var sideNav=document.getElementsByClassName('sidetoccontainer')[0];
    var main=document.getElementsByClassName('bodycontainer')[0];
    sideNav.style.display = "block";
    main.style.marginLeft = "15%";
    if (typeof(Storage) !== "undefined") {
        // Save the state of the sidebar as "open"
        localStorage.setItem("M216-sidebar", "opened");}
}

var closeSideNav = function(){
    var sideNav=document.getElementsByClassName('sidetoccontainer')[0];
    var main=document.getElementsByClassName('bodycontainer')[0];
    sideNav.style.display = "none";
    main.style.width="100%";
    if (typeof(Storage) !== "undefined") {
        // Save the state of the sidebar as "open"
        localStorage.setItem("M216-sidebar", "closed");
    }
}

var toggleSideNav = function(){
    var sideNav=document.getElementsByClassName('sidetoccontainer')[0];
    var main=document.getElementsByClassName('bodycontainer')[0];
    var sideNavDisplay=sideNav.style.display;
    if (sideNavDisplay == "block") {
	//close it
	closeSideNav();
    } else {
	openSideNav();
    }
}

var maybeOpenSideNav = function(){
    if (typeof(Storage) !== "undefined") {
        // If we need to open the bar
        if(localStorage.getItem("M216-sidebar") == "opened"){
	    openSideNav();
	}
    }
}

window.onload = function(){
    highlightCurrentSection(getNodeNum());
    addNavLinks(getNodeNum());
    maybeOpenSideNav()

}
