##MendelsFirst

##Given a number of homozygous dominant, heterozygous, and homozygous recessive individuals in a population, calculate the probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype).
##Input:

def receive_input():
    input_string = input("Enter the number of homozygous dominant, heterozygous, and homozygous recessive individuals (separated by spaces): ")
    return list(map(int, input_string.split()))

def calculate_probability(GG, Gg, gg):
    population_size = GG + Gg + gg

    #k_pairs
    k_pair_k = (GG / population_size) * ((GG - 1) / (population_size - 1))
    k_pair_m = (GG / population_size) * (Gg / (population_size - 1))
    k_pair_n = (GG / population_size) * (gg / (population_size - 1))
    
    #m pairs
    m_pair_m = (Gg / population_size) * ((Gg-1) / (population_size - 1)) * 0.75  
    m_pair_k = (Gg / population_size) * (GG / (population_size - 1))
    m_pair_n = (Gg / population_size) * (gg / (population_size - 1)) * 0.5

    #n pairs
    n_pair_m = (gg / population_size) * (Gg / (population_size - 1)) * 0.50
    n_pair_k = (gg / population_size) * (GG / (population_size - 1))

    probability = k_pair_k + k_pair_m + k_pair_n + m_pair_m + m_pair_k + m_pair_n + n_pair_m + n_pair_k
    return round(probability, 5)



def main():

    GG, Gg, gg = receive_input()
    probability = calculate_probability(GG, Gg, gg)
    print("The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele is:", probability)
if __name__ == "__main__":    main()