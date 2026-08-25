# from frappe.realtime import Socket, realtime


# @realtime.on("book_subscribe")
# def book_subscribe(socket: Socket, book: str) -> None:

#     print("BOOK SUBSCRIBE RECEIVED:", socket.user, book)

#     if socket.has_permission("Book", book):
#         socket.join(f"book:{book}")
#         print("JOINED ROOM:", f"book:{book}")