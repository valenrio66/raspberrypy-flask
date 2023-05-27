function showNotification(message, type) {
	Swal.fire({
		icon: type,
		text: message,
	});
}