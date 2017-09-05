package testmm;

import java.io.File;
import java.util.List;

import org.repodriller.domain.Commit;
import org.repodriller.persistence.PersistenceMechanism;
import org.repodriller.scm.CommitVisitor;
import org.repodriller.scm.RepositoryFile;
import org.repodriller.scm.SCMRepository;

import com.github.mauricioaniche.ck.CK;
import com.github.mauricioaniche.ck.CKNumber;
import com.github.mauricioaniche.ck.CKReport;

public class DevelopersVisitor2 implements CommitVisitor{

	@Override
	public void process(SCMRepository repo, Commit commit, PersistenceMechanism writer) {
		// TODO Auto-generated method stub
		try {
				int c = 0;
				System.out.println(repo.getPath());
				
				repo.getScm().checkout(commit.getHash());
				List<RepositoryFile> files = repo.getScm().files();
				CKReport report = new CK().calculate(repo.getPath());
				
				for(CKNumber result : report.all()) {
					System.out.println("");
					if(result.isError()) continue;
					if(!result.getFile().contains("test")) {
					writer.write(
						commit.getHash(),
						commit.getAuthor(),
						result.getFile() ,
						result.getClassName(),
						result.getType(),
						result.getCbo() ,
						result.getWmc() ,
						result.getDit() ,
						result.getNoc() ,
						result.getRfc() ,
						result.getLcom() ,
						result.getNom() ,
						result.getNopm() ,
						result.getNosm() ,
						result.getNof() ,
						result.getNopf() ,
						result.getNosf() ,
						result.getNosi() ,
						result.getLoc()
					);}
				}
		} finally {
			repo.getScm().reset();
		}
		
	}

	@Override
	public String name() {
		// TODO Auto-generated method stub
		return null;
	}

}
