import random

class Song:

  def __init__(self, song_id, name, artist, album):
    self.song_id = song_id
    self.name = name
    self.artist = artist
    self.album = album


class Node:

  def __init__(self, song):
    self.song = song
    self.next = None
    self.prev = None


class DoublyLinkedList:

  def __init__(self):
    self.head = None
    self.tail = None
    self.current_node = None
    self.current_song = None
    self.length = 0


  def __iter__(self):
    current_node = self.head
    while current_node:
      yield current_node
      current_node = current_node.next



  def __repr__(self):
    songs = ["PLAYLIST"]
    current_node = self.head
    while current_node is not None:
      songs.append(current_node.song.name)
      current_node = current_node.next

    songs.append('END')
    return " --> ".join(songs)


  def add_node(self, song):
    new_node = Node(song)
   
    if self.head is None:

      self.head = self.tail = new_node


    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
 
    self.length += 1

  
  def delete_node(self, node_value):
    current_node = self.head
   
    if current_node.song.name == node_value:
      
      self.head = self.head.next
      
      if self.head:
        self.head.prev = None

      
      else:
        self.tail = None
      self.length -= 1

      
      if self.current_node == current_node:
        self.current_node = None
        self.current_song = None
      return

    
    while current_node:
      
      if current_node.song.name == node_value:
        
        if current_node == self.tail:
          self.tail = current_node.prev
          
          self.tail.next = None

        else:
          
          current_node.prev.next = current_node.next
          
          current_node.next.prev = current_node.prev
        
        self.length -= 1

        
        if self.current_node == current_node:
          self.current_node = None
          self.current_song = None
        return
     
      current_node = current_node.next

  #primera cancion de la playlist
  def play(self):
    
    if self.head is not None:
      
      if self.current_song is None:
        
        self.current_node = self.head
      print("Playing:", self.current_node.song.name, "by",
            self.current_node.song.artist)
    else:
      print("Empty")

  
  def next(self):
    
    if self.current_node is not None and self.current_node != self.tail:
      
      self.current_node = self.current_node.next
      self.current_song = self.current_node.song
      print("Playing:", self.current_song.name, "by",
            self.current_song.artist)
    else:
      print(
        "empty"
      )

  
  def previous(self):
    
    if self.current_node is not None and self.current_node != self.head:
      
      self.current_node = self.current_node.prev
      self.current_song = self.current_node.song
      print("Playing:", self.current_song.name, "by",
            self.current_song.artist)
    else:
      print(
        "No previous"
      )


  def show_details(self):
   
    if self.current_node is not None and self.current_song is not None:
      print("ID:", self.current_song.song_id)
      print("Name:", self.current_song.name)
      print("Artist:", self.current_song.artist)
      print("Album:", self.current_song.album)
    else:
      print("error")

  
  def playlist_len(self):
    print('Length {} songs'.format(self.length))
    return self.length

  
  def play_shuffle(self):
    
    if self.head is not None:
      
      rand_song = random.choice(list(self))
      
      if rand_song is not None:
        self.current_song = rand_song.song
        print("Playing:", self.current_song.name, "by",
              self.current_song.artist)
    else:
      print(
        "empty"
      )

  
  def search_by_name(self, song_name):
    current_node = self.head
    while current_node:
      if current_node.song.name == song_name:
        self.current_song = current_node.song
        print("Playing", self.current_song.name, "by",
              self.current_song.artist)
        return
      current_node = current_node.next
    print("Not found")

  
  def search_by_artist(self, artist_name):
   
    songs_by_artist = []
    
    current_node = self.head
    while current_node:
      if current_node.song.artist == artist_name:
        
        songs_by_artist.append(current_node.song)
      
      current_node = current_node.next
    
    if len(songs_by_artist) > 0:
      print("Songs by", artist_name)

      
      for song in songs_by_artist:
        print("Name:", song.name)
        print("Album:", song.album)
    else:
      print("Not found")
