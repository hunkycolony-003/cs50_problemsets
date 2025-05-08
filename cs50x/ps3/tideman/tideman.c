#include <cs50.h>
#include <stdio.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX] = {{0}};

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool check_cycle(int i, int loser);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    // updates ranks[] returns true when name is present
    for (int i = 0; i < candidate_count; i++)
    {
        if (name == candidates[i])
        {
            ranks[rank] = i;
            return true;
        }
    }

    // Returns false if name is not present
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count - 1; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            preferences[ranks[i]][ranks[j]]++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    pair_count = 0;

    // Iterates over each opreferences to update pairs[]
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;
            }
            else if (preferences[i][j] < preferences[j][i])
            {
                pairs[pair_count].winner = j;
                pairs[pair_count].loser = i;
                pair_count++;
            }
        }
    }
    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // Sorts principle with bubble sort method wrt the votes of prefered candidate
    for (int i = 0; i < pair_count; i++)
    {
        int status = 0;
        for (int j = 0; j < pair_count - 1; j++)
        {
            int winner1 = pairs[j].winner;
            int loser1 = pairs[j].loser;

            int winner2 = pairs[j + 1].winner;
            int loser2 = pairs[j + 1].loser;

            // Skips iteration if neighbouring pairs have the same votes
            if (preferences[winner1][loser1] == preferences[winner2][loser2])
            {
                status = 1;
            }
            else if (preferences[winner1][loser1] < preferences[winner2][loser2])
            {
                status = 1;
                pair copy = pairs[j];
                pairs[j] = pairs[j + 1];
                pairs[j + 1] = copy;
            }
        }
        if (status == 0)
        {
            break;
        }
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        // Locks the first two pairs without any cycle-checks
        if (i < 2)
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }

        // Locks the pair if cycle is not present
        else if (!check_cycle(i, pairs[i].loser))
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    // Iterates over each candidate's edge status
    for (int i = 0; i < candidate_count; i++)
    {
        // tracks the status for each candidate
        bool status = true;

        // Updates status if any edge is terminated at the candidate
        for (int j = 0; j < candidate_count; j++)
        {
            // Avoids checking a candidate with themselves
            if (i == j)
            {
                continue;
            }
            if (locked[j][i])
            {
                status = false;
            }
        }

        /* Prints candidate if no edge is terminates at the candidate
           i.e. the source of the graph */
        if (status)
        {
            printf("%s\n", candidates[i]);
            return;
        }
    }
    return;
}

// Returns true is pairs[i] is creating cycle, else returns false
bool check_cycle(int i, int loser)
{
    if (pairs[i].winner == loser)
    {
        return true;
    }

    // Identifies if cycle present using recursion
    for (int j = i - 1; j > 0; j--)
    {
        if (pairs[i].winner == pairs[j].loser)
        {
            if (check_cycle(j, loser))
            {
                return true;
            }
        }
    }

    // Returns false if no cycle present
    return false;
}
