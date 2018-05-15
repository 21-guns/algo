package filesdemo;

import org.apache.commons.io.FileUtils;

import javax.swing.filechooser.FileSystemView;
import java.io.File;
import java.io.FilenameFilter;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Date;

public class FilesDemo {
    public static void main(String[] args) {
//        checkIfTheFileExists("file.txt");
//        copyADirectory("file.txt", "fileCopy.txt");
//        createADirectory();
//        deleteADirectory();
//        deleteADirectoryWithData();
//        deleteAFile();
//        fileCopying();
//        fileMoving();
//        getTheWorkingDirectory();
//        gettingFileProperties();
//        listOfFilesInTheDirectory();
        BinaryFilesDemo.readAndWriteUsingBuffer();
    }

    public static void checkIfTheFileExists(String fileName) {
        Path file = Paths.get(fileName);
        Boolean exists = Files.exists(file);
        System.out.println(exists);
    }

    public static void copyADirectory(String src, String dst) {
        File dir = new File(src);
        File dirCopy = new File(dst);

        try {
            FileUtils.copyDirectory(dir, dirCopy);
            System.out.println("Successfully copied");
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }

    public static void createADirectory() {
        File dir = new File("data");
        if (!dir.exists()) {
            dir.mkdir();
            System.out.println("Successfully Create");
        }
    }

    public static void deleteADirectory() {
        File dir = new File("data");
        if (dir.exists()) {
            dir.delete();
            System.out.println("Successfully Delete");
        }
    }

    public static void deleteADirectoryWithData() {
        File dir = new File("data_copy");
        try {
            if (dir.exists()) {
                FileUtils.deleteDirectory(dir);
                System.out.println("Successfully Deleted");
            } else {
                System.out.println("Dir not found");
            }
        }
        catch (Exception e) {
            System.out.println(e.toString());
        }
    }

    public static void deleteAFile() {
        Path file = Paths.get("file_copy.txt");
        try {
            if (Files.exists(file)) {
                Files.delete(file);
                System.out.println("Successfully Deleted");
            } else {
                System.out.println("file not found");
            }
        }
        catch (Exception e) {
            System.out.println(e.toString());
        }
    }

    public static void fileCopying() {
        Path file = Paths.get("file.txt");
        Path fileCopy = Paths.get("fileCopy.txt");
        try {
            Files.copy(file, fileCopy, StandardCopyOption.REPLACE_EXISTING);
        }
        catch (Exception e) {
            System.out.println(e.toString());
        }
    }

    public static void fileMoving() {
        Path file = Paths.get("file.txt");
        Path fileCopy = Paths.get("fileCopy.txt");
        try {
            Files.move(file, fileCopy, StandardCopyOption.REPLACE_EXISTING);
        }
        catch (Exception e) {
            System.out.println(e.toString());
        }
    }

    public static void getTheWorkingDirectory() {
        String path = FileSystemView
                .getFileSystemView()
                .getDefaultDirectory()
                .getPath();

        System.out.println(path);
    }

    public static void gettingFileProperties() {
        String filePath = "file.txt";
        File file = new File(filePath);
        long fileSize = file.length();
        Date dateChanges = new Date(file.lastModified());

        Boolean isReadable = file.canRead();
        Boolean isWriteable = file.canWrite();
        Boolean isExcuteable = file.canExecute();
        String fileDir = file.getParent();
    }

    public static void listOfFilesInTheDirectory() {
        File dir = FileSystemView
                .getFileSystemView()
                .getDefaultDirectory();

        File[] files = dir.listFiles(
                new FilenameFilter() {
                    @Override
                    public boolean accept(File dir, String name) {
                        return name.endsWith(".txt");
                    }
                }
        );
        for (File file: files) {
            System.out.println(file.getName());
        }
    }

}
