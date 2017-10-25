#include<sys/types.h>
#include<sys/socket.h>
#include<stdio.h>
#include<netinet/in.h> 
#include <unistd.h>
#include<string.h> 
#include <arpa/inet.h>
void main()
{
int b,udpsockfd,nBytes;
char buffer[10000];
char c[10000];
if((udpsockfd=socket(AF_INET,SOCK_DGRAM,0))>=0)  //socket creation
printf("socket created sucessfully \n");                 //on success 0 otherwise -1
struct sockaddr_in servaddr,clientaddr;              

//Assign server object parameters
servaddr.sin_family=AF_INET;
servaddr.sin_addr.s_addr=inet_addr("127.0.0.1");
servaddr.sin_port=6000;
//bind() assigns the
     //  address  specified  by  addr  to  the  socket  referred  to by the file
      // descriptor sockfd.  addrlen  specifies  the  size,  in  bytes,  of  the
     //  address structure pointed to by addr.  Traditionally, this operation is
      // called “assigning a name to a socket”.
if((b=bind(udpsockfd, (struct sockaddr *)&servaddr,sizeof(servaddr)))==0)   
printf("bind Sucessful \n");

int sin_size=sizeof(clientaddr);
recvfrom(udpsockfd,buffer,10000,0,(struct sockaddr *)&clientaddr, &sin_size);   

FILE *fp;
fp= fopen("/home/rajdeep/receive1.txt", "w+");


/* Read and display data */
fwrite(buffer,  1,strlen(buffer) + 1, fp);

printf("Received File Contents :%s \n", buffer);
fclose(fp);
close(udpsockfd);
}
