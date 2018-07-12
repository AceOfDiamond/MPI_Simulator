int main(int argc, char** argv) {
    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int number;
    if (world_rank==0)
    {
        CBLAS ( param )
        MPI_Send(&number, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
        MPI_Send(&number, 1, MPI_INT, 2, 0, MPI_COMM_WORLD);
        MM ( param )
    }
    else
    {
        Prod ( param )
        MPI_Recv(&number, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        CBLAS ( param )
    }
}