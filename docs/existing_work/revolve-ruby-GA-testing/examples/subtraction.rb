require File.join(File.dirname(__FILE__), "..", "revolve")

class Integer
  def protected_division(divisor)
    return 1 if divisor == 0
    self / divisor
  end
end

def cases(num, step, first, second)
  (1..num).map do |i|
    lambda do |program|
      my_first = first + step*i
      program.run( Revolve::Argument.new(:x, my_first), 
                   Revolve::Argument.new(:y, second)).to_i - (my_first - second)
    end
  end
end

# x - y
population = Revolve::Population.initialized( 200, {  
  :size_limit => 20,
  :instructions => [ Revolve::ERK.new(-5, -4, -3, -2, -1, 1, 2, 3, 4, 5),
                     Revolve::Method.new(:+), Revolve::Method.new(:-), 
                     Revolve::Method.new(:*), Revolve::Method.new(:protected_division),
                     Revolve::Variable.new(:x), Revolve::Variable.new(:y) ],
  :generations_limit => 500,                    
  :fitness_cases => cases(10, 6, 10, 34),
  :error_function => lambda{|cases| cases.inject{|x, y| x.abs + y.abs } },
  :elitism_percent => 0.35,
  :crossover_percent => 0.45,
  :mutation_percent => 0.1
})

population.evolve!

puts "Generations: #{population.generation}"
puts "Error: #{population.error(population.fittest)}"
puts "Program:\n#{population.fittest.inspect}"
input = [Revolve::Argument.new(:x, 900), Revolve::Argument.new(:y, 367)]
puts "Input: #{input}"
puts "Output: #{population.fittest.run(input)}"