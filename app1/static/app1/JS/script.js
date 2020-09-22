$(function () {
	$('[data-toggle="tooltip"]').tooltip();
});

//* Active Navs

const currentLocation = location.href;
const menuItem = document.querySelectorAll("a");
const menuLength = menuItem.length;
for (let i = 0; i < menuLength; i++) {
	if (menuItem[i].href === currentLocation) {
		// console.log(currentLocation);
		menuItem[i].className = "active nav-link";
	}
}
