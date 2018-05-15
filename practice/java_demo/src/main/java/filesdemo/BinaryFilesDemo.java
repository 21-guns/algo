package filesdemo;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;

public class BinaryFilesDemo {

    public static void readAndWriteUsingBuffer() {
        try {
            InputStream inputStream = new FileInputStream("file.out");
            OutputStream outputStream = new FileOutputStream("fileCopy.out");

            byte[] buffer = new byte[1024];
            int len;
            while ((len = inputStream.read(buffer)) != 1) {
                outputStream.write(buffer, 0, len);
            }
            inputStream.close();
            outputStream.close();
        }
        catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}
