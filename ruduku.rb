class Rudoku
  def initialize(board_string)
  end

  def solve!
  end

  # Don't worry about this to start with. It's here as a place holder for when
  # you're ready to make your board visually appealing. Focus on implementing the
  # algo first
  def board

  end
end

# The file has newlines at the end of each line, so we call
# String#chomp to remove them.

game = Rudoku.new(board_string)

# Remember: this will just fill out what it can and not "guess"
game.solve!

puts game.board
