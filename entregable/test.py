from linked_list import Node, Song, DoublyLinkedList


playlist = DoublyLinkedList()

song1 = Song(1, "SAFAERA", "BAD BUNNY", "UN VERANO SIN TI")
playlist.add_node(song1)

song2 = Song(2, "BABY SHARK", "COCOMELON", "ALBUM2")
playlist.add_node(song2)


song3 = Song(3, "CON ALTURA", "RRROSALIA", "ALBUM3")
playlist.add_node(song3)


song4 = Song(4, "YESTERDAY", "The BEATLES", "ALBUM4")
playlist.add_node(song4)
print(playlist)


playlist.delete_node("YESTERDAY")
print(playlist)

#play
playlist.play()

#next
playlist.next()

#ver detalles
playlist.show_details()

#prev
playlist.previous()



#next song
playlist.next()
playlist.next()



playlist.playlist_len()

'''


playlist.search_by_name("BABY SHARK")

#cuando no existe
playlist.search_by_name("ENSEÑAME A BAILAR")


playlist.search_by_artist("BAD BUNNY")



#play shuffle
playlist.play_shuffle()


print("----------------------------------------------")
print('Vamo a resetear la playlist')
print(playlist)
playlist.delete_node("I hope that you think of me")
print(playlist)


'''