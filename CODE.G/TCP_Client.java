import java.net.Socket;

public class TCP_Client {
    public static void main(String[] args) throws Exception {

        Socket Socket = new Socket("192.168.1.107", 7777);

        System.out.println("Hello");
    }
}

// import java.net.ServerSocket;

// class TCP_Server {
//     public static <Server> void main(String[] args) throws Exception {
//         ServerSocket ss = new ServerSocket(7777);

//         System.out.println("Server Waiting for Connection.....");

//         Object Sockets = ss.accept();

//         System.out.println("Hello");
//     }
// }
