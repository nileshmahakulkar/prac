#include<sys/types.h>
#include<sys/socket.h>
#include<stdio.h>
#include<netinet/in.h> 
#include <unistd.h>
#include<string.h> 
#include<strings.h>
#include <arpa/inet.h>
#include <stdlib.h>

void main()
{
int udpsockfd;

struct sockaddr_in servaddr,clientaddr;

// Socket call for socket creation: socket on sucess returns smallest integer value (3) otherwise -1
if((udpsockfd=socket(AF_INET,SOCK_DGRAM,0))>=0)
printf("Socket Created Sucessfully \n");


//Initialize object parameters of server: family,ip,port
servaddr.sin_family=AF_INET;
servaddr.sin_addr.s_addr=inet_addr("127.0.0.1");
servaddr.sin_port=6000;

//initiate a connection on a socket from client to server using connect call
// connect call on sucess return 0 otnerwise -1


char buffer[100];
char c[10000] = "this is file transfer program using UDP";
//char source[MAXBUFLEN + 1];
//bzero(buffer,10000);

FILE *fp; 
fp= fopen("/home/rajdeep/send1.txt", "w+");


   /* Write data to the file */
   fwrite(c, 1, strlen(c) + 1, fp);

   /* Seek to the beginning of the file */
   fseek(fp, 0, SEEK_SET);

   /* Read and display data */
   fread(buffer, 1,strlen(c)+1, fp);
  int len=strlen(buffer);
  // fclose(fp);
sendto(udpsockfd,buffer,len,0,(struct sockaddr *)&servaddr,sizeof(servaddr));
//write(connfd, buffer, strlen(buffer));
printf("Sent File Contents: %s\n", buffer);
fclose(fp);

close(udpsockfd);
} 
